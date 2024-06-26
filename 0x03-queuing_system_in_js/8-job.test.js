import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import { createQueue } from 'kue';

// PART 2: SETTING UP THE TEST SUITE

describe('createPushNotificationsJobs function', () => {
  const CONSOLE_SPY = sinon.spy(console);

  // Create a queue (task) for testing purposes
  const TASK = createQueue({ name: 'push_notification_code_test' });

  // Before all tests, enter test mode
  before(() => {
    TASK.testMode.enter(true);
  });

  // After all tests, clear the queue and exit mode
  after(() => {
    TASK.testMode.clear();
    TASK.testMode.exit();
  });

  // After each test, reset the history of the spy
  afterEach(() => {
    CONSOLE_SPY.log.resetHistory();
  });

  // PART 3: TESTING ERROR HANDLING
  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, TASK)
    ).to.throw('Jobs is not an array');
  });

  // PART 4: TESTING FOR JOB ADDITION
  it('adds jobs (task) to the queue with the correct type', (done) => {
    // Initially, the queue should be empty
    expect(TASK.testMode.jobs.length).to.equal(0);

    // Define the task information to add to the queue
    const jobInfo = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];

    // Add jobs (tasks) to the queue
    createPushNotificationsJobs(jobInfo, TASK);

    // Check that two jobs were added to the queue
    expect(TASK.testMode.jobs.length).to.equal(2);
    expect(TASK.testMode.jobs[0].data).to.deep.equal(jobInfo[0]);
    expect(TASK.testMode.jobs[0].type).to.equal('push_notification_code_3');

    // Process the queue and check console log for job creation
    TASK.process('push_notification_code_3', () => {
      expect(
        CONSOLE_SPY.log.calledWith(
          'Notification job created:', TASK.testMode.jobs[0].id
        )
      ).to.be.true;
      done();
    });
  });

  // PART 5: TESTING EVENT HANDLERS
  it('registers the progress event handler for a job', (done) => {
    // Add a listener for the progress event
    TASK.testMode.jobs[0].addListener('progress', () => {
      expect(
        CONSOLE_SPY.log.calledWith(
          'Notification job', TASK.testMode.jobs[0].id, '25% complete'
        )
      ).to.be.true;
      done();
    });

    // Emit a progress event with 25% completion
    TASK.testMode.jobs[0].emit('progress', 25);
  });

  it('registers the failed event handler for a job', (done) => {
    // Add a listener for the failed event
    TASK.testMode.jobs[0].addListener('failed', () => {
      expect(
        CONSOLE_SPY.log.calledWith(
          'Notification job', TASK.testMode.jobs[0].id, 'failed:', 'Failed to send'
        )
      ).to.be.true;
      done();
    });

    // Emit a failed event with an error message
    TASK.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('registers the complete event handler for a job', (done) => {
    // Add a listener for the complete event
    TASK.testMode.jobs[0].addListener('complete', () => {
      expect(
        CONSOLE_SPY.log.calledWith(
          'Notification job', TASK.testMode.jobs[0].id, 'completed'
        )
      ).to.be.true;
      done();
    });

    // Emit a complete event
    TASK.testMode.jobs[0].emit('complete');
  });
});

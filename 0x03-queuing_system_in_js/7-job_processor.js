import { createQueue } from 'kue';

const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue(); // Create a new job queue

/**
 * Function to send a push notification to a user.
 * @param {String} phoneNumber - The recipient's phone number
 * @param {String} message - The message to send
 * @param {Job} job - The job object representing the notification task
 * @param {Function} done - The callback to call when the job is complete
 */
const sendNotification = (phoneNumber, message, job, done) => {
  const totalSteps = 2; // Total number of progress steps
  let remainingSteps = 2; // Remaining progress steps

  const sendInterval = setInterval(() => { // Create an interval timer that runs every second
    if (totalSteps - remainingSteps <= totalSteps / 2) { // Track initial progress (0% to 50%)
      job.progress(totalSteps - remainingSteps, totalSteps);
    }

    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) { // Check if the phone number is blacklisted
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval); // Stop the interval timer
      return;
    }

    if (totalSteps === remainingSteps) { // On the first interval execution
      console.log(`Sending notification to ${phoneNumber},`,
        `with message: ${message}`);
    }

    remainingSteps -= 1;
    if (remainingSteps === 0) done();
    if (remainingSteps === 0) clearInterval(sendInterval); // Stop the interval timer
  }, 1000);
};

// Set up the queue to process 'push_notification_code_2' jobs, handling 2 jobs concurrently
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

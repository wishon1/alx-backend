import { createQueue } from 'kue';

const queue = createQueue();

const jobData = queue.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

jobData
  .on('enqueue', () => {
    console.log('Notification job created:', jobData.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });

jobData.save();

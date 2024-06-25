import kue from 'kue';

const queueInstance = kue.createQueue();

// the function to send the notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// process the job from the queue
queueInstance.process('push_notification_code', (task, done) => {
  sendNotification(task.data.phoneNumber, task.data.message);
  done();
});

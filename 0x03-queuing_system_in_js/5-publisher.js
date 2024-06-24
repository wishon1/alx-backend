import { createClient } from 'redis';

const clientInstance = createClient();

clientInstance
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

/**
 * Publishes a message to the 'holberton school channel' after a specified delay.
 * @param {string} message - The message to publish.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    clientInstance.publish('holberton school channel');
  }, time);
}

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Call the function with specified messages and delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);

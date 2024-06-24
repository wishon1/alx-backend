import { createClient } from 'redis';

const clientInstance = createClient();

clientInstance
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

// suscribe to holberton schhol channel
clientInstance.subscribe('holberton school channel');

clientInstance.on('message', (message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    clientInstance.unsubscribe('holberton school channel');
    clientInstance.quit();
  }
});

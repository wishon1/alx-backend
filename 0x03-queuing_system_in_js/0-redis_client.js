/**
 *  should connect to the Redis server running on your machine:
 * It should log to the console the message Redis client connected to the server
 * when the connection to Redis works correctly It should log to the console the
 * message Redis client not connected to the server: ERROR_MESSAGE when the
 * connection to Redis does not work
 */
import { createClient } from 'redis';

const clientInstance = createClient();

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

clientInstance.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

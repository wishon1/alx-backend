/**
 *  should connect to the Redis server running on your machine:
 * It should log to the console the message Redis client connected to the server
 * when the connection to Redis works correctly It should log to the console the
 * message Redis client not connected to the server: ERROR_MESSAGE when the
 * connection to Redis does not work
 */
import { createClient, print } from 'redis';

const clientInstance = createClient();

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

clientInstance.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

/**
 * Sets a new school in Redis.
 * @param {string} schoolName - The name of the school.
 * @param {string} value - The value to set for the school.
 */
function setNewSchool(schoolName, value) {
  clientInstance.set(schoolName, value, print);
}

/**
 * Displays the value of a school from Redis.
 * @param {string} schoolName - The name of the school to display.
 */
function displaySchoolValue(schoolName) {
  clientInstance.get(schoolName, (_, reply) => {
    console.log(reply);
  });
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

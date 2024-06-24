import { createClient, print } from 'redis';

const clientInstance = createClient();

clientInstance.on('connect', () => {
  console.log('Redis client connected to the server');
});

clientInstance.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// create hash
clientInstance.hset('HolbertonSchools', 'Portland', '50', print);
clientInstance.hset('HolbertonSchools', 'Seattle', '80', print);
clientInstance.hset('HolbertonSchools', 'New York', '20', print);
clientInstance.hset('HolbertonSchools', 'Bogota', '20', print);
clientInstance.hset('HolbertonSchools', 'Cali', '40', print);
clientInstance.hset('HolbertonSchools', 'Paris', '2', print);

// Display hash
clientInstance.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.log(`${err}`);
    throw err;
  } else {
    console.log(result);
  }
});

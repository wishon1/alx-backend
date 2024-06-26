import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// Create an array of products
const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

// Create an express app
const app = express();
const PORT = 1245;

// Create a Redis client and promisify get/set methods
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Route to get the list of products
app.get('/list_products', (_, res) => {
  const formattedProducts = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));
  res.json(formattedProducts);
});

// Function to reserve stock by ID
function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

// Function to get the current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10); // Convert the itemId to an integer
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId) || item.stock;
  return res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10); // Convert the itemId to an integer
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(itemId) || item.stock;
  if (currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, currentStock - 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

// Start the express server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

import axios from 'axios';

// Admin Dashboard API
export default axios.create({
  baseURL: 'http://localhost:5000',
});
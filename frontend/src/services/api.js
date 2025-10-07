import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const getBooks = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/books/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching books:', error);
    throw error;
  }
};

export const getBookById = async (id) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/books/${id}/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching book:', error);
    throw error;
  }
};

export const getAuthors = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/authors/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching authors:', error);
    throw error;
  }
};
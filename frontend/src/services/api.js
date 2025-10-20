const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const api = {
  getBooks: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    const url = `${API_BASE_URL}/books/${queryString ? '?' + queryString : ''}`;
    
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Status ${response.status}`);
    }
    return response.json();
  },

  getBook: async (id) => {
    const response = await fetch(`${API_BASE_URL}/books/${id}/`);
    if (!response.ok) {
      throw new Error(`Status ${response.status}`);
    }
    return response.json();
  },

  getAuthors: async () => {
    const response = await fetch(`${API_BASE_URL}/authors/`);
    if (!response.ok) {
      throw new Error(`Status ${response.status}`);
    }
    return response.json();
  },

  getPublishers: async () => {
    const response = await fetch(`${API_BASE_URL}/publishers/`);
    if (!response.ok) {
      throw new Error(`Status ${response.status}`);
    }
    return response.json();
  },
};
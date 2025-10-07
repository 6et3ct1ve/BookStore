import React, { useState, useEffect } from 'react';
import { getBooks } from './services/api';
import './App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      setLoading(true);
      const data = await getBooks();
      setBooks(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch books. Make sure the Django server is running on port 8000.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="container"><h2>Loading...</h2></div>;
  }

  if (error) {
    return (
      <div className="container">
        <h2 style={{ color: 'red' }}>Error</h2>
        <p>{error}</p>
        <button onClick={fetchBooks}>Retry</button>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>📚 BookStore</h1>
        <p>Fetching data from Django API (demonstrating CORS)</p>
      </header>
      
      <div className="container">
        <h2>Books ({books.length})</h2>
        
        {books.length === 0 ? (
          <p>No books found. Add some books in Django admin!</p>
        ) : (
          <div className="books-grid">
            {books.map(book => (
              <div key={book.id} className="book-card">
                <img 
                  src={book.cover_image} 
                  alt={book.title}
                  className="book-cover"
                />
                <h3>{book.title}</h3>
                <p className="author">by {book.author.name}</p>
                <p className="publisher">Publisher: {book.publisher.name}</p>
                <p className="genre">{book.genre}</p>
                <p className="price">${book.price}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
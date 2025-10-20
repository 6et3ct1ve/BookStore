import React, { useState, useEffect } from 'react';
import BookCard from '../components/js/BookCard';
import SearchBar from '../components/js/SearchBar';
import ErrorMessage from '../components/js/Error';
import Loading from '../components/js/Loading';
import { api } from '../services/api';

function BooksPage() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useState({});

  useEffect(() => {
    loadBooks();
  }, [searchParams]);

  const loadBooks = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getBooks(searchParams);
      setBooks(data.results || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} />

      {loading && <Loading />}
      
      {error && <ErrorMessage message={error} />}

      {!loading && !error && books.length === 0 && (
        <div className="no-books">
          <p>NO BOOKS FOUND</p>
        </div>
      )}

      {!loading && !error && books.length > 0 && (
        <div className="book-list">
          {books.map(book => (
            <BookCard key={book.id} book={book} />
          ))}
        </div>
      )}
    </div>
  );
}

export default BooksPage;
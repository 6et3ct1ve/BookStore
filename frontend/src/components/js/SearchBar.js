import React, { useState } from 'react';
import '../css/SearchBar.css';

function SearchBar({ onSearch }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [genre, setGenre] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ search: searchTerm, genre });
  };

  return (
    <form className="search-bar" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Search by title or author..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="search-input"
      />
      
      <select 
        value={genre} 
        onChange={(e) => setGenre(e.target.value)}
        className="genre-select"
      >
        <option value="">All Genres</option>
        <option value="Fantasy">Fantasy</option>
        <option value="Dark fantasy">Dark Fantasy</option>
        <option value="Science Fiction">Science Fiction</option>
        <option value="Mystery">Mystery</option>
        <option value="Romance">Romance</option>
        <option value="Thriller">Thriller</option>
      </select>

      <button type="submit" className="search-button">
        Search
      </button>
    </form>
  );
}

export default SearchBar;
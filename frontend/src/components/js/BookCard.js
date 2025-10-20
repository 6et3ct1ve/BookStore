import React from 'react';
import '../css/BookCard.css';

function BookCard({ book }) {
  return (
    <div className="book-card">
      {book.cover_image && (
        <img 
          src={book.cover_image} 
          alt={book.title}
          className="book-cover"
        />
      )}
      <h3>{book.title}</h3>
      <p className="author">
        <strong>Author:</strong> {book.author.name}
      </p>
      <p className="price">
        <strong>Price:</strong> ₴{book.price}
      </p>
      <p className="genre">
        <strong>Genre:</strong> {book.genre}
      </p>
    </div>
  );
}

export default BookCard;
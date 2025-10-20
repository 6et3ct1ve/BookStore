import React from 'react';
import { Link } from 'react-router-dom';
import '../css/Header.css';

function Header() {
  return (
    <header className="stalker-header">
      <div className="header-container">
        <div className="header-title">
          <h1>BOOKSTORE</h1>
        </div>
        
        <nav className="header-nav">
          <Link to="/" className="nav-link">
            BOOKS
          </Link>
          <Link to="/authors" className="nav-link">
            AUTHORS
          </Link>
          <Link to="/publishers" className="nav-link">
            PUBLISHERS
          </Link>
        </nav>
      </div>
    </header>
  );
}

export default Header;
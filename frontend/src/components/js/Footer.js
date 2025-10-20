import React from 'react';
import '../css/Footer.css';

function Footer() {
  return (
    <footer className="stalker-footer">
      <div className="footer-container">
        <div className="footer-scan">
          <span className="scan-line"></span>
        </div>
        
        <div className="footer-content">
          <p className="footer-text">
            2025 | <span className="footer-author">BUTSKO BOHDAN</span>
          </p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
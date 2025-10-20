import React from 'react';
import '../css/Loading.css';

function Loading() {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Wait...</p>
    </div>
  );
}

export default Loading;
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/js/Layout';
import BooksPage from './pages/BooksPage';
import AuthorsPage from './pages/AuthorsPage';
import PublishersPage from './pages/PublishersPage';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<BooksPage />} />
          <Route path="/authors" element={<AuthorsPage />} />
          <Route path="/publishers" element={<PublishersPage />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
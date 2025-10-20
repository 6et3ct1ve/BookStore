import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import Loading from '../components/js/Loading';
import ErrorMessage from '../components/js/Error';

function AuthorsPage() {
  const [authors, setAuthors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadAuthors();
  }, []);

  const loadAuthors = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAuthors();
      setAuthors(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <Loading />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <div>
      <h2 className="page-title">AUTHORS</h2>
      <div className="authors-grid">
        {authors.map(author => (
          <div key={author.id} className="author-card">
            <h3>{author.name}</h3>
            <p><strong>Birth Year:</strong> {author.birth_year || 'Unknown'}</p>
            <p><strong>Nationality:</strong> {author.nationality || 'Unknown'}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AuthorsPage;
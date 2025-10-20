import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import Loading from '../components/js/Loading';
import ErrorMessage from '../components/js/Error';

function PublishersPage() {
  const [publishers, setPublishers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadPublishers();
  }, []);

  const loadPublishers = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getPublishers();
      setPublishers(data);
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
      <h2 className="page-title">PUBLISHERS</h2>
      <div className="authors-grid">
        {publishers.map(publisher => (
          <div key={publisher.id} className="author-card">
            <h3>{publisher.name}</h3>
            <p><strong>Website:</strong> {publisher.website || 'N/A'}</p>
            <p><strong>Country:</strong> {publisher.country || 'Unknown'}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PublishersPage;
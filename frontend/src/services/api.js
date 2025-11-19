import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' }
});

export const generateFactions = async (count) => {
  const response = await api.get(`/factions/${count}`);
  return response.data;
};

export const generateQuest = async (factions = null) => {
  const response = await api.post('/quests/',
    factions ? { factions } : {}
  );
  return response.data;
};

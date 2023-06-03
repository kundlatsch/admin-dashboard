import React from 'react';

import './App.css';
import Routing from './routes';
import { AuthProvider } from './context/AuthContext';
import Home from './pages/Home'

function App() {
  return (
    <AuthProvider>
      <Routing />
    </AuthProvider>
  )
}

export default App;
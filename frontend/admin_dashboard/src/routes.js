import React from 'react';
import { Navigate, Route, BrowserRouter, Routes } from 'react-router-dom';

import Home from './pages/Home';

const Routing = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}/>
        <Route path='*' element={Home}/>
      </Routes>
    </BrowserRouter>
  )
};

export default Routing;
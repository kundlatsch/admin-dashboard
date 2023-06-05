import React from 'react';
import { Navigate, Route, BrowserRouter, Routes } from 'react-router-dom';

import Home from './pages/Home';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import NewClient from './pages/NewClient';
import EditClient from './pages/EditClient';

const Routing = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Dashboard />}/>
        <Route path='/login' element={<Home />}/>
        <Route path='/register' element={<Register />}/>
        <Route path='/new_client' element={<NewClient />}/>
        <Route path='/edit_client/:client_id' element={<EditClient />}/>
        {/* <Route path='/dashboard' element={<Dashboard />}/> */}
        <Route path='*' element={Home}/>
      </Routes>
    </BrowserRouter>
  )
};

export default Routing;
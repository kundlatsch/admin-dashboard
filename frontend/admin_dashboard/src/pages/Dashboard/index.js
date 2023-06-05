import React, { useState, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import './styles.css';
import { Context } from '../../context/AuthContext';
import adminAPI from '../../services/adminAPI';
import Card from './components/Card';


function Dashboard() {

  const { authenticated, handleLogout } = useContext(Context);

  const [clients, setClients] = useState([]);

  let navigate = useNavigate();

  const navigateToNewClient = () => {
    navigate("/new_client");
  };

  const getClientData = async () => {
    try {
      const { data } = await adminAPI.get(`/clients/`);
      return data
    }
    catch (err) {
      return []
    }
  }

  useEffect(() => {
    if (!authenticated) {
      navigate("/");
    }
    
    getClientData().then(data => setClients(data));
    
  });

  const handleLogoutClick = () => {
    handleLogout();
    navigate("/");
  }

  return (
    <div className="center-container" id="user-home">
      <div className="default-container">

        <div className="buttons-container">
          <div>
            <h1>Admin Dashboard</h1>
          </div>

          <button
            type="submit" 
            className="orange-button"
            onClick={navigateToNewClient}
          >
            Add new client
          </button>
        </div>

        <div className="client-container">
          {
            clients.map(client => {
              return <Card
                id={client.id}
                name={client.name}
                cpf={client.cpf}
                rg={client.rg}
                rg_state={client.rg_state}
                date_of_birth={client.date_of_birth}
                phone_number={client.phone_number}
              ></Card>
            }
            )
          }
          
        </div>

        <p onClick={handleLogoutClick}>
          Logout
        </p>

      </div>
    </div>
  )
}

export default Dashboard
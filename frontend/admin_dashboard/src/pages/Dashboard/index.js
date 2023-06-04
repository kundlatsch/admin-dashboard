import React, { useState, useEffect, useContext } from 'react';
import { FiPlus } from 'react-icons/fi';
import { useNavigate } from 'react-router-dom';

import './styles.css';
import { Context } from '../../context/AuthContext';
import adminAPI from '../../services/adminAPI';
import Card from './components/Card';


function Dashboard() {

  const { authenticated, globalUsername, handleLogout } = useContext(Context);

  const [username, setUsername] = useState("");
  const [clients, setClients] = useState([]);
  const [weekDayNumber, setWeekdayNumber] = useState();
  const [dayAnime, setDayAnime] = useState([]);
  const [dialogOpen, setDialogOpen] = useState(false);

  let navigate = useNavigate();

  let card_data = {
    id: 1,
    name: "Gustavo",
    cpf: "11551827905",
    rg: "6663708",
    rg_state: "ssp-sc",
    date_of_birth: "26/09/1999",
    phone_number: "48 999527764"
  }

  const handleClickDialogOpen = () => {
    setDialogOpen(true);
  };

  const handleDialogClose = () => {
    setDialogOpen(false);
  };

  // const handleDialogReturn = (newAnime) => {
  //   if (newAnime.animeWeekDay == weekDayNumber) {
  //     setDayAnime([...dayAnime, newAnime]);
  //   }
  // }

  const navigateToHistory = () => {
    navigate("/");
  };

  const getClientData = async () => {
    const { data } = await adminAPI.get(`/clients/`);
    if (!data) {
      return [];
    }
    return data;
  }

  useEffect(() => {
    if (!authenticated) {
      navigate("/");
    }
    setUsername(globalUsername);
    
    getClientData().then(data => setClients(data));
    
  }, []);

  const handlePlusClick = async (anime) => {
    const updateId = anime.id;
    const newCurrentEpisode = anime.currentEpisode + 1;

    if (anime.currentEpisode <= anime.totalEpisodes) {
      // await adminAPI.put(`animes/watch/${anime.id}`);
    }

    const updateAnimeList = (dayAnime.map(animeMap => {
      return animeMap.id === updateId && newCurrentEpisode <= animeMap.totalEpisodes ? 
        { ...animeMap, currentEpisode: newCurrentEpisode }: animeMap
    }));
    setDayAnime(updateAnimeList);
  }

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
            className="green-button"
            onClick={navigateToHistory}
          >
            Add new client
          </button>
        </div>

        <div className="anime-container">
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
import React, { useState, useContext, useEffect } from 'react'
import { useNavigate, useParams, useLocation, Link } from 'react-router-dom';
import { FiArrowLeft } from 'react-icons/fi';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';

import { Context } from '../../context/AuthContext';
import adminAPI from '../../services/adminAPI';

import './styles.css';

function EditClient() {

  let { client_id } = useParams();
  let { state } = useLocation();
  const { name, cpf, rg, rg_state, date_of_birth, phone_number } = state;

  let navigate = useNavigate();
  const { authenticated } = useContext(Context);
  const MySwal = withReactContent(Swal);

  useEffect(() => {
    if (!authenticated) {
      navigate("/");
    }
  });

  const handleUpdateClient = () => {
    adminAPI.patch(`/clients/${client_id}`, {
      name: nameState,
      cpf: cpfState,
      rg: rgState,
      rg_state: rgStateState,
      phone_number: phoneNumberState,
      date_of_birth: dateOfBirthState,
    }).then(res => {
      MySwal.fire({
        icon: 'success',
        title: 'Successs!',
        text: 'The client was successfully updated.',
      });
      navigate("/dashboard");
    }).catch(err => {
      let message = err.response.data.message
      if (!message) message = 'Verify the informed values and try again'
      MySwal.fire({
        icon: 'error',
        title: 'Something went wrong...',
        text: message,
      });
    });
  }

  const handleCreateAddress = () => {
    adminAPI.post(`/addresses/${client_id}`, {
      address,
      complement,
      city,
      state: addressState
    }).then(res => {
      MySwal.fire({
        icon: 'success',
        title: 'Successs!',
        text: 'Address added to the client.',
      });
      navigate("/dashboard");
    }).catch(err => {
      let message = err.response.data.message
      if (!message) message = 'Verify the informed values and try again'
      MySwal.fire({
        icon: 'error',
        title: 'Something went wrong...',
        text: message,
      });
    });
  }

  const [nameState, setNameState] = useState(name);
  const [cpfState, setCpfState] = useState(cpf);
  const [rgState, setRgState] = useState(rg);
  const [rgStateState, setRgStateState] = useState(rg_state);
  const [dateOfBirthState, setDateOfBirthState] = useState(date_of_birth);
  const [phoneNumberState, setPhoneNumberState] = useState(phone_number);
  const [address, setAddress] = useState("");
  const [complement, setComplement] = useState("");
  const [city, setCity] = useState("");
  const [addressState, setAddressState] = useState("");


  return (
    <div className="center-container">
      <div className="default-container" id="edit-client">
        <Link to='/dashboard' className='return-button'>
            <FiArrowLeft />
            Return
        </Link>
        <h1>Edit client #{client_id}: {name}</h1>
        <div className="edit-client-columns">
          <div className='edit-client-column'>
          <label>Name</label>
            <input 
              type="text"
              className="default-input"
              placeholder={name}
              value={nameState}
              onChange={(e) => {
                setNameState(e.target.value);
              }}
            />

            <label>CPF</label>
            <input 
              type="text"
              className="default-input"
              placeholder={cpf}
              value={cpfState}
              onChange={(e) => {
                setCpfState(e.target.value);
              }}
            />

            <label>RG</label>
            <input 
              type="text"
              className="default-input"
              placeholder={rg}
              value={rgState}
              onChange={(e) => {
                setRgState(e.target.value);
              }}
            />
          </div>
          <div className='edit-client-column'>
            <label>RG issuing body</label>
            <input 
              type="text"
              className="default-input"
              placeholder={rg_state}
              value={rgStateState}
              onChange={(e) => {
                setRgStateState(e.target.value);
              }}
            />

            <label>Date of birth</label>
            <input 
              type="text"
              className="default-input"
              placeholder={date_of_birth}
              value={dateOfBirthState}
              onChange={(e) => {
                setDateOfBirthState(e.target.value);
              }}
            />

            <label>Phone number</label>
            <input 
              type="text"
              className="default-input"
              placeholder={phone_number}
              value={phoneNumberState}
              onChange={(e) => {
                setPhoneNumberState(e.target.value);
              }}
            />
          </div>
        </div>

        <button
          className="orange-button"
          onClick={handleUpdateClient}
        >
          Update Client
        </button>

        <hr/>

        <h1>Add new address</h1>

        <div className="edit-client-columns">
          <div className='edit-client-column'>
          <label>Address</label>
            <input 
              type="text"
              className="default-input"
              value={address}
              onChange={(e) => {
                setAddress(e.target.value);
              }}
            />

            <label>Complement</label>
            <input 
              type="text"
              className="default-input"
              value={complement}
              onChange={(e) => {
                setComplement(e.target.value);
              }}
            />
          </div>
          <div className='edit-client-column'>
            <label>City</label>
            <input 
              type="text"
              className="default-input"
              value={city}
              onChange={(e) => {
                setCity(e.target.value);
              }}
            />

            <label>State</label>
            <input 
              type="text"
              className="default-input"
              value={addressState}
              onChange={(e) => {
                setAddressState(e.target.value);
              }}
            />

          </div>
        </div>

        <button
          className="orange-button"
          onClick={handleCreateAddress}
        >
          Save address
        </button>
        
      </div>
    </div>
    
  )
}

export default EditClient
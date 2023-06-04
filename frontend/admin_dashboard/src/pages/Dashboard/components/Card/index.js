import React, { useState, useEffect } from 'react';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';

import adminAPI from '../../../../services/adminAPI';
import './styles.css';

export default function Card({id, name, cpf, rg, rg_state, date_of_birth, phone_number}) {

    const [isActive, setIsActive] = useState(false);
    const [displayContent, setDisplayContent] = useState(false);
    const [addresses, setAddresses] = useState([]);
    const [deleted, setDeleted] = useState(false)

    const MySwal = withReactContent(Swal);

    const handleDelete = () => {
        MySwal.fire({
          title: 'Do you want to delete permanently this client?',
          showDenyButton: true,
          showCancelButton: true,
          showConfirmButton: false,
          denyButtonText: `Delete`,
          }).then((result) => {
          if (result.isDenied) {
            adminAPI.delete(`/clients/${id}`).then(data => {
              MySwal.fire('Client deleted', '', 'success')
              setDeleted(true)
            });
          }
        })
    }

    const getClientAddresses = async () => {
        try {
            const { data } = await adminAPI.get(`/addresses/${id}`);
            data.forEach((element, index, arr) => {
                delete element["client_id"]
                delete element["id"]
                let values = Object.values(element)
                values = values.filter(e => e !== '' && e !== null);
                arr[index] = values.join(", ")
            });
            console.log(data)
            return data
        } catch(err) {
            console.log("erro")
            return []
        }
      }
    
      useEffect(() => {
        
        getClientAddresses().then(data => setAddresses(data));
        
      }, []);

    let handleOpenCard = () => {
        if (isActive) {
            setIsActive(false)
            setDisplayContent(false)
        }
        else {
            setIsActive(true)
            setDisplayContent(true)
        }
    }

    return <div className={deleted ? 'deleted' : 'card'}>
        <button 
            type="button" 
            className={isActive ? 'collapsible-card active-card' : 'collapsible-card'} 
            onClick={handleOpenCard}
        >
            {`${id}  -  ${name}`}
        </button>
        <div className={displayContent ? 'content-card-active' : 'content-card-inactive'}>
            <div className='card-attribute'>
                <b>ID:</b> {`${id}`}
            </div>
            <div className='card-attribute'>
                <b>Name:</b> {`${name}`}
            </div>
            <div className='card-attribute'>
                <b>CPF:</b> {`${cpf}`}
            </div>
            <div className='card-attribute'>
                <b>RG:</b> {`${rg}`}
            </div>
            <div className='card-attribute'>
                <b>RG issuing body:</b> {`${rg_state}`}
            </div>
            <div className='card-attribute'>
                <b>Date of birth:</b> {`${date_of_birth}`}
            </div>
            <div className='card-attribute'>
                <b>Phone number:</b> {`${phone_number}`}
            </div>
            {
              addresses.map(address => {
                return <div className='card-attribute'>
                    {address}
                </div>
              })
            }
            <div className='card-attribute card-clickable card-edit'>
                <b>Edit Client</b>
            </div>
            <div className='card-attribute card-clickable card-delete' onClick={handleDelete}>
                <b>Delete Client</b>
            </div>
        </div> 
    </div>
}
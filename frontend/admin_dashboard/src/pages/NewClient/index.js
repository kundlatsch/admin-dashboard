import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';

import './styles.css';
import adminAPI from '../../services/adminAPI';

const NewClient = () => {

  let navigate = useNavigate();
  const MySwal = withReactContent(Swal);

  const initialValues = {
    Email: "",
    Username: "",
    Password: "",
  }

  const validationSchema = Yup.object().shape({
    Name: Yup.string().required().min(1).max(50),
    CPF: Yup.string().required().min(11).max(15),
    RG: Yup.string().required().min(6),
    RGState: Yup.string(),
    PhoneNumber: Yup.string().required(),
    DateOfBirth: Yup.string().required(),
    Address: Yup.string().required(),
    Complement: Yup.string(),
    City: Yup.string(),
    State: Yup.string()
  });

  const handleCreateClient = (data) => {
    console.log("salve")
    adminAPI.post('/clients/', {
      name: data.Name,
      cpf: data.CPF,
      rg: data.RG,
      rg_state: data.RGState,
      phone_number: data.PhoneNumber,
      date_of_birth: data.DateOfBirth,
      address: data.Address,
      complement: data.Complement,
      city: data.City,
      state: data.State

    }).then(res => {
      MySwal.fire({
        icon: 'success',
        title: 'Successs!',
        text: 'The client was added to the database.',
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
  };

  return (
    <div className="center-container">
      <div className="default-container">
        <h1>Add new client</h1>
          <Formik
            initialValues={initialValues}
            onSubmit={handleCreateClient}
            validationSchema={validationSchema}
          >
            <Form className='form-base-container'>
            <div className="form-create-client">
            <div className='form-container-create-client'>
              
              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="Name" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input"
                  name="Name"
                  type="text"
                  placeholder="Name"
              />

              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="CPF" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input"
                  name="CPF"
                  type="text"
                  placeholder="CPF"
              />
              
              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="RG" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input" 
                  name="RG"
                  type="text"
                  placeholder="RG"
              />

              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="RGState" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input" 
                  name="RGState"
                  type="text"
                  placeholder="RG issuing body"
              />

              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="PhoneNumber" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input" 
                  name="PhoneNumber"
                  type="text"
                  placeholder="Phone number"
              />

              <div className="vspace5"></div>
              <div className="vspace20">
                  <ErrorMessage name="DateOfBirth" component="span" />
              </div>
              <Field 
                  className="default-input create-client-input" 
                  name="DateOfBirth"
                  type="text"
                  placeholder="Date of birth"
              />
            </div>

            <div className='form-container-create-client'>

              <div className="vspace5"></div>
                <div className="vspace20">
                    <ErrorMessage name="Address" component="span" />
                </div>
                <Field 
                    className="default-input create-client-input"
                    name="Address"
                    type="text"
                    placeholder="Address"
                />
              
                <div className="vspace5"></div>
                <div className="vspace20">
                    <ErrorMessage name="Complement" component="span" />
                </div>
                <Field 
                    className="default-input create-client-input"
                    name="Complement"
                    type="text"
                    placeholder="Complement"
                />

                <div className="vspace5"></div>
                <div className="vspace20">
                    <ErrorMessage name="City" component="span" />
                </div>
                <Field 
                    className="default-input create-client-input"
                    name="City"
                    type="text"
                    placeholder="City"
                />

                <div className="vspace5"></div>
                <div className="vspace20">
                    <ErrorMessage name="State" component="span" />
                </div>
                <Field 
                    className="default-input create-client-input"
                    name="State"
                    type="text"
                    placeholder="State"
                />

            </div>

            </div>
            <button
                type="submit" 
                className="green-button"
                id="create-client-button"
            >
                Create client
            </button>

            </Form>
          </Formik>
        
      </div>
    </div>
   
  )
};

export default NewClient;
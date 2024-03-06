import React, { useState } from "react";
import Card from "../card";
import "./Test.css";
import axios from "axios";
const Test = () => {
  const [dataForm, setDataForm] = useState([]);
  const [dataSubmit, setDataSubmit] = useState("");
  const onSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted");
    increaseNumber();
  };

  const increaseNumber = () => {
    //mandorespuesta y recojo la pregunta
    if (dataForm.length == 0) {
      axios.get(`http://127.0.0.1:8000/start`).then((response) => {
        setDataForm(response.data);
        console.log(dataForm);
      });
    } else {
      const newDataForm = [""];
      axios
        .post(`http://127.0.0.1:8000/response/${dataSubmit}`, {
          data: newDataForm,
        })
        .then((response) => {
          // Save the response data to dataForm
          console.log("hola estoy en el post");
          setDataForm(response.data);
          console.log(dataForm);
        })
        .catch((error) => {
          console.error(error);
          // Handle the error
        });
      // let lastValue =
      //   newDataForm.length > 0 ? newDataForm[newDataForm.length - 1] : 0;
      // newDataForm.push(lastValue + 1);
      // Agregar un nuevo elemento al final del array con un valor distinto
      if (dataForm.image_url || dataForm.Error) {
        console.log("holi");
        window.location.reload();
      }
    }
  };

  return (
    <>
      <img src="" alt="" />
      <form onSubmit={onSubmit}>
        {dataForm.detail ? (
          <div className="formulario">
            <div>
              <Card item={dataForm.detail} setDataForm={setDataSubmit} />
            </div>
          </div>
        ) : (
          <img src="/imagen.gif" alt="" className="imagen" />
        )}

        <button className="btn" type="submit">
          <strong>{dataForm.length !== 0 ? "RESPONDER" : "INICIAR"}</strong>
          <div id="container-stars">
            <div id="stars"></div>
          </div>

          <div id="glow">
            <div className="circle"></div>
            <div className="circle"></div>
          </div>
        </button>
      </form>
    </>
  );
};

export default Test;

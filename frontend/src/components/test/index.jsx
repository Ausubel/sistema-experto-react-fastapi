import React, { useState } from "react";
import Card from "../card";
import "./Test.css";
import axios from "axios";
const Test = () => {
  const [dataForm, setDataForm] = useState([]);
  const [dataSubmit, setDataSubmit] = useState("2");
  const onSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted");
    increaseNumber();
  };

  const increaseNumber = () => {
    //mandorespuesta y recojo la pregunta
    const newDataForm = [...dataForm];
    axios
      .post(`http://127.0.0.1:8000/response/${dataSubmit}`, { data: newDataForm })
      .then((response) => {
        // Save the response data to dataForm
        setDataForm([response.data]);
      })
      .catch((error) => {
        console.error(error);
        // Handle the error
      });
    // let lastValue =
    //   newDataForm.length > 0 ? newDataForm[newDataForm.length - 1] : 0;
    // newDataForm.push(lastValue + 1);
    // Agregar un nuevo elemento al final del array con un valor distinto
  };

  return (
    <>
      <img src="" alt="" />
      <form onSubmit={onSubmit}>
        {dataForm.length > 0 ? (
          <div className="formulario">
            {dataForm.map((item, index) => {
              return (
                <div key={index}>
                  <Card item={item} setDataForm={setDataSubmit} />
                </div>
              );
            })}
          </div>
        ) : (
          <img src="/imagen.gif" alt="" className="imagen" />
        )}

        <button class="btn" type={"submit"}>
          <strong>{dataForm.length > 0 ? "RESPONDER" : "INICIAR"}</strong>
          <div id="container-stars">
            <div id="stars"></div>
          </div>

          <div id="glow">
            <div class="circle"></div>
            <div class="circle"></div>
          </div>
        </button>
      </form>
    </>
  );
};

export default Test;

import React, { useState } from "react";
import Card from "../card";
import "./Test.css";
const Test = () => {
  const [dataForm, setDataForm] = useState([]);
  const [dataSubmit, setDataSubmit] = useState("");
  const onSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted");
    increaseNumber();
    console.log(dataSubmit);
  };

  const increaseNumber = () => {
    const newDataForm = [...dataForm];

    let lastValue =
      newDataForm.length > 0 ? newDataForm[newDataForm.length - 1] : 0;
    newDataForm.push(lastValue + 1); // Agregar un nuevo elemento al final del array con un valor distinto
    setDataForm(newDataForm);
  };

  return (
    <>
      <form onSubmit={onSubmit}>
        {dataForm.length > 0 ? (
          <div className="formulario">
            {dataForm.map((item, index) => {
              return (
                <div key={index}>
                  <Card item={item} setDataForm={setDataSubmit} />
                  {/* <button onClick={increaseNumber}>Aumentar</button> */}
                </div>
              );
            })}
          </div>
        ) : (
          <img src="/imagen.gif" alt="" className="imagen"/>
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

        {/* <button onClick={() => console.log(dataForm)}>mostrar</button> */}
      </form>
    </>
  );
};

export default Test;

import React, { useState } from "react";
import "./Card.css";
import "./checkbox.css";

const Card = ({ item, setDataForm }) => {
  const [selectedOptions, setSelectedOptions] = useState({});

  const handleCheckboxChange = (option) => {
    setSelectedOptions({
      ...selectedOptions,
      [item]: option,
    });
    setDataForm(option);
  };

  return (
    <div className="card">
      <div className="card__content">
        <h2>Pregunta</h2>
        <p>¿{item}?</p>
        <div className="cuadroCheck">
          <label>
            <div className="col-md-6 reject-checkbox">
              <div className="mb-2 text-center">
                <div className="checkbox-wrapper">
                  <input
                    name="ehs_approval"
                    className="form-check-label custom-radio-label"
                    id={`rejected-${item}`}
                    type="checkbox"
                    checked={selectedOptions[item] === "si"}
                    onChange={() => handleCheckboxChange("si")}
                  />
                  <label htmlFor={`rejected-${item}`}>
                    <div className="tick_mark">
                      <div className="cross"></div>
                    </div>
                  </label>
                </div>
              </div>
            </div>
          </label>{" "}
          <div className="checkbox-wrapper">
            <input
              id={`accepted-${item}`}
              type="checkbox"
              checked={selectedOptions[item] === "no"}
              onChange={() => handleCheckboxChange("no")}
            />
            <label htmlFor={`accepted-${item}`}>
              <div className="tick_mark"></div>
            </label>
          </div>{" "}
        </div>
      </div>
    </div>
  );
};

export default Card;

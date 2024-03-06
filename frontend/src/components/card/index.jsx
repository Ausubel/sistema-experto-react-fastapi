import React, { useState } from "react";
import "./Card.css";
import "./checkbox.css";

const Card = ({ item, setDataForm }) => {
  const [selectedOptions, setSelectedOptions] = useState({});
  console.log(item);
  const handleCheckboxChange = (option) => {
    setSelectedOptions({
      ...selectedOptions,
      [item]: option,
    });
    setDataForm(option);
    console.log(option);
  };

  return (
    <>
      <div className="card">
        <div className="card__content">
          {item.detail.description || item.detail.Error ? (
            <>
              <p>{item.detail.name}</p>
              <p>
                {item.detail.description
                  ? item.detail.description
                  : item.detail.Error}
              </p>
              {item.detail.description ? (
                <img src={item.detail.image_url} alt="" />
              ) : (
                ""
              )}
            </>
          ) : (
            <>
              {" "}
              <h2>Pregunta</h2>
              <p>¿{item.detail.name}?</p>
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
                          checked={selectedOptions[item] === 0}
                          onChange={() => handleCheckboxChange(0)}
                        />
                        <label htmlFor={`rejected-${item}`}>
                          <div className="tick_mark">
                            <div className="cross"></div>
                          </div>
                        </label>
                      </div>
                    </div>
                  </div>
                </label>
                <div className="checkbox-wrapper">
                  <input
                    id={`accepted-${item}`}
                    type="checkbox"
                    checked={selectedOptions[item] === 1}
                    onChange={() => handleCheckboxChange(1)}
                  />
                  <label htmlFor={`accepted-${item}`}>
                    <div className="tick_mark"></div>
                  </label>
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </>
  );
};

export default Card;

import { useState } from "react";
import Test from "./components/test";
import "./fondo.css";
function App() {
  return (
    <>
      <div className="main">
        <Test></Test>
      </div>

      <div className="fondo">
        <div className="rain rain1"></div>
        <div className="rain rain2">
          <div className="drop drop2"></div>
        </div>
        <div className="rain rain3"></div>
        <div className="rain rain4"></div>
        <div className="rain rain5">
          <div className="drop drop5"></div>
        </div>
        <div className="rain rain6"></div>
        <div className="rain rain7"></div>
        <div className="rain rain8">
          <div className="drop drop8"></div>
        </div>
        <div className="rain rain9"></div>
        <div className="rain rain10"></div>
        <div className="drop drop11"></div>
        <div className="drop drop12"></div>
      </div>
      
    </>
  );
}

export default App;

import { useState } from 'react'
import './App.css'
import axios from 'axios'
import Button from "@mui/material/Button"

function App() {
  const [message, setMessage] = useState("Click Me")

  return (
    <>
      <h1>Testing Hello world</h1>
      <div className="card">
        <Button  className="Button" variant="outlined" onClick={() => {
            axios.get('http://localhost:8000/api/')
                .then( response => {
                    console.log(response);
                    setMessage(response.data["status"]);
                } ).catch(error => {
                    console.log(error);
            })
        }}>
          {message}
        </Button>
      </div>
    </>
  )
}

export default App

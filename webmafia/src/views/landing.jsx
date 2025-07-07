import '../App.css'
import axios from 'axios'
import Button from "@mui/material/Button"
import Grid from '@mui/material/Grid';

function Landing() {
    return (
        <>
            <div className="card">
                <h1>Welcome To The Mafia Game</h1>

                <Grid container spacing={2}>
                   <Grid size={12}>
                       <Button  className="Button" variant="outlined" onClick={() => {
                           axios.get('http://localhost:8000/api/')
                               .then( response => {
                                   console.log(response);
                               } ).catch(error => {
                               console.log(error);
                           })
                       }}>
                           Create Game
                       </Button>
                   </Grid>
                    <Grid size={12}>
                        <Button  className="Button" variant="outlined" onClick={() => {
                            axios.get('http://localhost:8000/api/')
                                .then( response => {
                                    console.log(response);
                                } ).catch(error => {
                                console.log(error);
                            })
                        }}>
                            Join Game
                        </Button>
                    </Grid>
                </Grid>
            </div>
        </>
    )
}

export default Landing

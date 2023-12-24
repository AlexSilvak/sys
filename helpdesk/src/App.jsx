import { useState , useEffect} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {
  const [count, setCount] = useState(0)
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState();
  


  useEffect(() => {
    fetch("http://127.0.0.1:5000/home")
      .then(res => res.json())
      .then(
        (result) => {
          
        setItems(result);

        console.log(items)
         
         
        } ,
      
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])

return(

  <>
  
 
<form action="http://127.0.0.1:5000/home" method="GET">

<label className='lbemail'><span className="material-symbols-outlined">
person
</span><input type='email' className='input'></input></label>

<br></br>
<br></br>
<label className='lbpasswd' ><span className="material-symbols-outlined">
lock
</span><input type='password' className='input'></input></label>
<p><button type="submit" >Login</button></p>
</form>
  
  
  
  </>
)




}

export default App

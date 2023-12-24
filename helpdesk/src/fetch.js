import { useState , useEffect} from 'react'


function fetch() {

 
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);
  
  
    useEffect(() => {
      fetch("http://127.0.0.1:5000/home")
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setItems(result);
           console.log(result)
            
          },
        
          (error) => {
            setIsLoaded(true);
            setError(error);
          }
        )
    }, [])
  

  
  
  
  }
  
  export default fetch
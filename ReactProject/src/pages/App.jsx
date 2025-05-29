import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import JobBoard from '../pages/JobBoard';
import NewPage from '../pages/NewPage'
import { Box } from '@mui/material';
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';
function App() {
  const Navbar = () => (
    <nav 
    style={{ 
      position: 'fixed',
      padding: '1px',
      top: '0',
      left: '0',
      }}>

      <Box
      sx={{
      
      paddingX: '75px',
      border: '2px solid',
      borderRadius: '3px',
      borderColor: 'white',
      
      }}
      >

      <h2>This should carry over between the two pages</h2>
      <Stack direction="row" spacing={2}  divider={<Divider orientation="vertical" flexItem />}
      sx={{
        border: '2px solid',
        padding: '20px'
      }}
      >
      <h2>one</h2>
      <h2>two</h2>
      <h2>three</h2>
      </Stack>

   

      <Link to="/jobs">Jobs </Link>
      <Link to="/newPage">new page</Link>
      </Box>

    </nav>
  );

  return (
    <Router>

      <Routes>
        
        <Route
          path="/jobs"
          element={
            <>
              <Navbar />
              <JobBoard />
            </>
          }
        />
        <Route
          path="/newPage"
          element={
            <>
              <Navbar />
              <NewPage/>
            </>
          }
        />
        <Route
          path="/"
          element={
            <>
            <h1>Sign in</h1>
            <Link to="/jobs"><h2>This is where the sign in box would go</h2></Link>
            </>

          }
        />
      </Routes>
    </Router>
  );
}

export default App
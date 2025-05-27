import { useState } from 'react'
import CardBox from './CardBox.jsx';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Stack from '@mui/material/Stack'
import { Divider } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import './App.css'

const theme = createTheme({
  palette: {
    mode: 'dark', // Add dark mode for better visibility with dark background
    background: {
      default: '#0b1020',
      paper: '#215636'
    },
    primary: {
      main: '#09335B'
    },
    secondary: {
      main: '#215636'
    }
  },
});



function App() {
  const [count, setCount] = useState(0)

  return (
    <ThemeProvider theme={theme}>
      <div style={{ minHeight: '100vh', padding: '2rem' }}>
        <h1 style={{ color: 'white', marginBottom: '2rem' }}>ISE jobs board</h1>

        <Stack 
          direction="column"
          spacing={3}
          divider={
            <Divider 
              orientation="horizontal"
              flexItem
              sx={{
                borderColor: 'rgba(255, 255, 255, 0.3)'
              }}
            />
          }
        >
          <CardBox/>
          <CardBox/>
          <CardBox/>
          <CardBox/>
        </Stack>
      </div>
    </ThemeProvider>
  )
}

export default App
import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { useTheme } from '@mui/material/styles'; 
import { CardHeader, Divider } from '@mui/material';
import Avatar from '@mui/material/Avatar';
import { deepOrange, deepPurple } from '@mui/material/colors';

export default function CardBox() {
  const avatarText = "R1/2";

  const colorMap = {
    "R1": { avatar: '#2e7d32', card: '#2FD537' },       // green
    "R1/2": { avatar: '#1565c0', card: '#1680F8' },      // blue
    "R2": { avatar: '#6a1b9a', card: '#921ED9' },        // purple
    "Default": { avatar: '#757575', card: '#eeeeee' },  // gray
  };

  const colors = colorMap[avatarText] || colorMap["Default"];

  const theme = useTheme(); 
  const CardDivider = (
    <Box
    sx = {{
      paddingX: '20px'
    }}
    >
    <Divider
      orientation="vertical"
      flexItem
      sx={{
        borderColor: 'rgba(255, 255, 255, 0.3)',
        height: '100%', 
      }}
    />
    </Box>

  );

  return (
    <Card
      variant="outlined"
      sx={{
        textAlign: 'start',
        padding: '5px',
        width: '60rem', 
        height: '155px',
        borderRadius: '4px 45px 4px 4px',
        backgroundColor: colors.card,      }}
    >
      
      <Box
      sx = {{

        height: '65px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}
      > 
      <Box
  sx={{
    display: 'flex',
    alignItems: 'center',
    height: '50px', 
    paddingX: 2,
  }}
>
  <Box sx={{ flex: 1, 
  padding: 'px',
  }}
  >
     <Avatar
              sx={{
                bgcolor: colors.avatar,
                height: '50px',
                width: '50px',
              }}
            >
              {avatarText}
            </Avatar> </Box>
  
  <Box
  sx = {{
    height: '100%',
    paddingX: '15px'
  }}
  >
  <Divider
    orientation="vertical"
    flexItem
    sx={{
      borderColor: 'rgba(255, 255, 255, 0.3)',
      height: '100%',
    }}
  />
  </Box>

<Box sx={{ flex: 100, 
  padding: '15px',
  
  }}
  >
    <h2 style={{ margin: 0 }}>Name here </h2>
  </Box>

</Box>




      </Box>

      <Divider
      orientation='horizontal'
      />

      <CardContent
        sx={{
          padding: '10px',
          display: 'flex',
          alignItems: 'top', 
          justifyContent: 'space-between',
          height: '100px', 
        }}
      >
        
        <div style={{ flex: 1, textAlign: 'center' }}>
          <h3>Job Title</h3>
        </div>
        {CardDivider}
        <div style={{ flex: 1, textAlign: 'center' }}>
          <h3>Other Thing</h3>
        </div>
        {CardDivider}
        <div style={{ flex: 1, textAlign: 'center' }}>
          <p>Job description and details go here...</p>
        </div>
      </CardContent>
    </Card>
  ); 
}
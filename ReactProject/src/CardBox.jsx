import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { useTheme } from '@mui/material/styles'; 
import { CardHeader, Divider } from '@mui/material';

export default function CardBox() {
  const theme = useTheme(); 
  const cardDivider = (
    <Divider
      orientation="vertical"
      flexItem
      sx={{
        borderColor: 'rgba(255, 255, 255, 0.3)',
        height: '100%', 
      }}
    />
  );

  return (
    <Card
      variant="outlined"
      sx={{
        textAlign: 'left',
        width: '60rem', 
        height: '155px',
        borderRadius: '4px 45px 4px 4px',
        backgroundColor: theme.palette.background.paper, 
      }}
    >

      <Box
      sx = {{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}
      > 
      <CardHeader
      title = "Joblmao"
      sx = {{flex: 1,}}
      />

      <Divider
      orientation='vertical'
      flexItem
      sx ={{height: 'auto',}}
      />



      </Box>

      <Divider
      orientation='horizontal'
      />

      <CardContent
        sx={{
          display: 'flex',
          alignItems: 'top', 
          justifyContent: 'space-between',
          height: '100px', 
        }}
      >
        
        <div style={{ flex: 1, textAlign: 'center' }}>
          <h3>Job Title</h3>
        </div>
        {cardDivider}
        <div style={{ flex: 1, textAlign: 'center' }}>
          <h3>Other Thing</h3>
        </div>
        {cardDivider}
        <div style={{ flex: 1, textAlign: 'center' }}>
          <p>Job description and details go here...</p>
        </div>
      </CardContent>
    </Card>
  ); 
}
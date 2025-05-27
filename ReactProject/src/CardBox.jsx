import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { useTheme } from '@mui/material/styles'; 
import { Divider } from '@mui/material';

export default function CardBox() {
  const theme = useTheme(); 
  const cardDivider = (
    <Divider
    orientation="vertical"
    flexItem
    sx={{
      borderColor: 'rgba(255, 255, 255, 0.3)'
    }}
     />
  );
  return (
    <Card
      variant="outlined"
      sx={{
        textAlign: 'left',
        width: '60rem',
        padding: '2rem', 
        minHeight: '100px',
        borderRadius: ' 4px 45px 4px 4px  ',
        backgroundColor: theme.palette.background.paper, 
      }}
    >
      <CardContent>
        <h3>Job Title</h3>
        {cardDivider}
        <p>Job description and details go here...</p>
      </CardContent>
    </Card>
  ); 
}
import React from 'react';
import { useAuth } from './AuthContext';
import { Box, Button, Heading, Text } from '@chakra-ui/react';
import Layout from './Layout';

export default function Dashboard() {
  const { logout } = useAuth();

  return (
    <Layout>
      <Box p={8}>
        <Heading as="h1" size="lg" mb={6}>
          Dashboard
        </Heading>
        <Text mb={4}>Welcome to your dashboard!</Text>
        <Button colorScheme="blue" onClick={logout}>
          Logout
        </Button>
      </Box>
    </Layout>
  );
}

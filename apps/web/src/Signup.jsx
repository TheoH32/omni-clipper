import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Input,
  Heading,
  Text,
  useToast,
  VStack,
} from '@chakra-ui/react';

export default function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [accessCode, setAccessCode] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const toast = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await axios.post('http://localhost:8000/signup', {
        email,
        password,
        access_code: accessCode,
      });
      toast({
        title: 'Success',
        description: 'Account created successfully. Please login.',
        status: 'success',
        duration: 5000,
        isClosable: true,
      });
      navigate('/login');
    } catch (err) {
      toast({
        title: 'Error',
        description: 'Failed to sign up. Please check your details.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
    setLoading(false);
  };

  return (
    <Box maxW="md" mx="auto" mt={10} p={8} borderWidth={1} borderRadius="lg">
      <Heading as="h1" size="lg" textAlign="center" mb={6}>
        Sign Up
      </Heading>
      <form onSubmit={handleSubmit}>
        <VStack spacing={4}>
          <FormControl isRequired>
            <FormLabel>Email</FormLabel>
            <Input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </FormControl>
          <FormControl isRequired>
            <FormLabel>Password</FormLabel>
            <Input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </FormControl>
          <FormControl isRequired>
            <FormLabel>Access Code</FormLabel>
            <Input
              type="text"
              value={accessCode}
              onChange={(e) => setAccessCode(e.target.value)}
            />
          </FormControl>
          <Button type="submit" colorScheme="blue" width="full" isLoading={loading}>
            Sign Up
          </Button>
        </VStack>
      </form>
      <Text textAlign="center" mt={4}>
        Already have an account?{' '}
        <Link to="/login" style={{ color: '#3182ce' }}>
          Login
        </Link>
      </Text>
    </Box>
  );
}

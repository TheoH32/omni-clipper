import React, { useState } from 'react';
import { useAuth } from './AuthContext';
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
  InputGroup,
  InputRightElement
} from '@chakra-ui/react';
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';
import Layout from './Layout';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false); // New state for password visibility
  const { login } = useAuth();
  const navigate = useNavigate();
  const toast = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await login(email, password);
      navigate('/');
    } catch (err) {
      toast({
        title: 'Error',
        description: 'Failed to login. Please check your credentials.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
    setLoading(false);
  };

  const handleGoogleLogin = () => {
    const code = prompt('Please enter the access code:');
    if (code === '1024') {
      window.location.href = `${import.meta.env.VITE_API_URL}/auth/youtube`;
    } else {
      toast({
        title: 'Error',
        description: 'Incorrect access code.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
  };

  return (
    <Layout>
      <Box maxW="md" mx="auto" mt={10} p={8} borderWidth={1} borderRadius="lg" bg="brand.900">
        <Heading as="h1" size="lg" textAlign="center" mb={6}>
          Login
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
              <InputGroup>
                <Input
                  type={showPassword ? 'text' : 'password'}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <InputRightElement width="4.5rem">
                  <Button h="1.75rem" size="sm" onClick={() => setShowPassword(!showPassword)}>
                    {showPassword ? <ViewOffIcon /> : <ViewIcon />}
                  </Button>
                </InputRightElement>
              </InputGroup>
            </FormControl>
            <Button type="submit" colorScheme="blue" width="full" isLoading={loading}>
              Login
            </Button>
          </VStack>
        </form>
        <Text textAlign="center" my={4}>
          Or
        </Text>
        <Button colorScheme="red" width="full" onClick={handleGoogleLogin}>
          Login with Google
        </Button>
        <Text textAlign="center" mt={4}>
          Don't have an account?{' '}
          <Link to="/signup" style={{ color: '#3182ce' }}>
            Sign up
          </Link>
        </Text>
      </Box>
    </Layout>
  );
}

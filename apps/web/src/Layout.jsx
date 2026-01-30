import React from 'react';
import { Box, Flex, Heading, Text } from '@chakra-ui/react';

export default function Layout({ children }) {
  return (
    <Box>
      <Flex
        as="header"
        align="center"
        justify="space-between"
        wrap="wrap"
        padding="1.5rem"
        bg="brand.900"
        color="white"
      >
        <Flex align="center" mr={5}>
          <Heading as="h1" size="lg" letterSpacing={'-.1rem'}>
            Omni Clipper
          </Heading>
        </Flex>
      </Flex>
      <Box as="main" p={8}>
        {children}
      </Box>
      <Box as="footer" py={4} textAlign="center" bg="brand.900" color="white">
        <Text>&copy; {new Date().getFullYear()} Omni Clipper. All rights reserved.</Text>
      </Box>
    </Box>
  );
}

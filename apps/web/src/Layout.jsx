import React from 'react';
import {
  Box,
  Flex,
  Heading,
  Text,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  IconButton,
  Avatar,
  MenuDivider,
} from '@chakra-ui/react';
import { useAuth } from './AuthContext';
import { HamburgerIcon } from '@chakra-ui/icons';

export default function Layout({ children }) {
  const { isAuthenticated, user } = useAuth();

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

        {isAuthenticated && (
          <Menu>
            <MenuButton
              as={Avatar}
              size="sm"
              cursor="pointer"
              name={user?.name}
              src="https://bit.ly/dan-abramov" // Placeholder image
            />
            <MenuList color="black">
              <Box p="2">
                <Text fontWeight="bold">{user?.name}</Text>
                <Text fontSize="sm">{user?.email}</Text>
              </Box>
              <MenuDivider />
              <MenuItem>
                Settings
              </MenuItem>
              <MenuItem>
                User Profile
              </MenuItem>
            </MenuList>
          </Menu>
        )}
      </Flex>
      <Box as="main" p={8}>
        {children}
      </Box>
      <Box as="footer" py={4} textAlign="center" bg="brand.900" color="white">
              </Box>
    </Box>
  );
}

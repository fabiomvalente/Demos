package com.cursojava.mongodb.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cursojava.mongodb.domain.User;
import com.cursojava.mongodb.dto.UserDTO;
import com.cursojava.mongodb.repository.UserRepository;
import com.cursojava.mongodb.services.exception.ObjectNotFoundException;

@Service
public class UserService {

    @Autowired
    private UserRepository repo;

    public List<User> findAll() {
        return repo.findAll();
    }

    public User findById(String id) {
        return repo.findById(id).orElseThrow(() -> new ObjectNotFoundException("Usuário não Encontrado"));
    }

    public User insert(User obj) {
        return repo.insert(obj);
    }

    public void delete(String id) {
        findById(id);
        repo.deleteById(id);
    }

    public User update(User obj) {
        User newObj = findById(obj.getId());
        updateData(newObj, obj);
        return repo.save(newObj);
    }
    private void updateData(User newObj, User obj) {
        newObj.setName(obj.getEmail());
        newObj.setEmail(obj.getEmail());        
    }

    public User fromDTO(UserDTO objDto) {
        return new User(objDto.getId(), objDto.getName(), objDto.getEmail());
    }
}

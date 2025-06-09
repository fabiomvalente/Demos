package com.cursojava.mongodb.services;

import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cursojava.mongodb.domain.Post;
import com.cursojava.mongodb.repository.PostRepository;
import com.cursojava.mongodb.services.exception.ObjectNotFoundException;

@Service
public class PostService {

    @Autowired
    private PostRepository repo;

    public Post findById(String id) {
        return repo.findById(id).orElseThrow(() -> new ObjectNotFoundException("Usuário não Encontrado"));
    }
    
    public List<Post> findByTitle(String text) {
        return repo.searchTitle(text);
    }

    public List<Post> fullsearch(String text, Date minDate, Date maxDate) {
        maxDate = new Date(maxDate.getTime() + 24 * 60 * 60 * 1000);
        return repo.fullSearch(text, minDate, maxDate);
    }
}

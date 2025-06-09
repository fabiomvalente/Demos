package com.cursojava.mongodb.resources.exception;

import java.time.Instant;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import com.cursojava.mongodb.services.exception.ObjectNotFoundException;

import jakarta.servlet.http.HttpServletRequest;

@ControllerAdvice
public class ResourceExceptionHandler {

    @ExceptionHandler(ObjectNotFoundException.class)
    public ResponseEntity<StandardError> objetctNotFound(ObjectNotFoundException e, HttpServletRequest request) {
        HttpStatus status = HttpStatus.NOT_FOUND;
        // O 1o parâmetro eu mudei de Long para Instant para ser mais legível aos usuários
        StandardError err = new StandardError(Instant.now(), status.value(), "Não encontrado", e.getMessage(), request.getRequestURI());
        return ResponseEntity.status(status).body(err);
    }
}
